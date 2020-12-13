import time
import sys
from src import main
from watchdog.observers import Observer
from watchdog.events import RegexMatchingEventHandler
from IPython.lib.deepreload import reload

exclude = (
    'sys',
    'os',
    'os.path',
    'builtins',
    '__main__',
    'numpy',
    'numpy._globals',
    'json',
    're',
    'enum',
    'types',
    'functools',
    'collections',
    'operator',
    'keyword',
    'heapq',
    'itertools',
    'codecs',
    'distutils',
    'errno',
    'distutils.dir_util',
    'distutils.errors'
)


class EventHandler(RegexMatchingEventHandler):
    def __init__(self):
        super().__init__(regexes=[
            r'.*\.py$',
            r'.*\.json$',
        ], ignore_regexes=[
            r'.*package.json$',
            r'.*env\\',
            r'.*venv\\',
            r'.*node_modules\\',
            r'.*vscode\\'
        ], case_sensitive=True)

    def on_modified(self, event):
        print(f"{event.event_type}: {event.src_path}")
        reload(main, exclude=exclude)
        main.generate_files()


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if sys.argv[1] == "dev":
            my_event_handler = EventHandler()

            my_observer = Observer()
            my_observer.schedule(my_event_handler, "./src", recursive=True)

            my_observer.start()
            try:
                print("Watching files for changes...")
                main.generate_files()
                while True:
                    time.sleep(5)
            except KeyboardInterrupt:
                my_observer.stop()
                print("Observer Stopped")
            my_observer.join()
        elif sys.argv[1] == "build":
            main.generate_files()
        else:
            print("unknown argument", sys.argv[1])
    else:
        print("\nUsage: python3 run.py <command>\n\nwhere <command> is one of:\n\tbuild, dev\n")
