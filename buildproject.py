import os
import subprocess
import shutil

def main():
    try:
        os.makedirs('dist', exist_ok=True)

        # Install dependencies
        print("Installing dependencies...")
        subprocess.check_call(['python', '-m', 'pip', 'install', '-r', 'requirements.txt'])

        # Collect static files
        print("Collecting static files...")
        subprocess.check_call(['python', 'manage.py', 'collectstatic', '--noinput', '--clear'])

        # Copy build artifacts to the dist directory
        # Assuming the build artifacts are generated in a directory named 'build'
        if os.path.exists('build'):
            print("Copying build artifacts to 'dist'...")
            for item in os.listdir('build'):
                s = os.path.join('build', item)
                d = os.path.join('dist', item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, dirs_exist_ok=True)
                else:
                    shutil.copy2(s, d)
        else:
            print("Error: Build artifacts directory 'build' not found.")
            exit(1)

        print("Project built successfully!")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing a subprocess: {e}")
        exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(1)

if __name__ == "__main__":
    main()