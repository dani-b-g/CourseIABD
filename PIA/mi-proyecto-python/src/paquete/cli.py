def main():
    import argparse

    parser = argparse.ArgumentParser(description="Interfaz de línea de comandos para mi proyecto.")
    parser.add_argument('--run', action='store_true', help='Ejecuta la aplicación.')
    
    args = parser.parse_args()

    if args.run:
        from .app import App
        app = App()
        app.run()
    else:
        parser.print_help()