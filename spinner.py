import sys, asyncio

# spinning_cursor yields the current cursor for the spinner
def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

# spin runs a ASCII spinner in CLI to indicate its still running.
async def spin():
    spinner = spinning_cursor()
    while(1):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        await asyncio.sleep(0.1)
        sys.stdout.write('\b')