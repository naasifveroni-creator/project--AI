"""
Entry point. Choose an interface:

    python main.py cli
    python main.py api
    python main.py discord
"""
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [cli|api|discord]")
        sys.exit(1)

    mode = sys.argv[1].lower()

    if mode == "cli":
        from src.interfaces.cli import run
        run()
    elif mode == "api":
        import uvicorn
        from src import config
        uvicorn.run("src.interfaces.api:app", host=config.API_HOST, port=config.API_PORT, reload=True)
    elif mode == "discord":
        from src.interfaces.discord_bot import run
        run()
    else:
        print(f"Unknown mode: {mode}")
        print("Usage: python main.py [cli|api|discord]")
        sys.exit(1)


if __name__ == "__main__":
    main()
