import subprocess
import os

def main():
    # Ensure the output directory exists
    if not os.path.exists('dist'):
        print("Creating output directory 'dist'...")
        os.makedirs('dist')

    # Install dependencies
    print("Installing dependencies...")
    subprocess.check_call(['python','-m', 'pip', 'install', '-r', 'requirements.txt'])

    # COllect static files
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
                subprocess.check_call(['cp', '-r', s, d])
            else:
                subprocess.check_call(['cp', s, d])
    else:
        print("Error: Build artifacts directory 'build' not found.")
        exit(1)

    print("Project built successfully!")

if __name__ == "__main__":
    main()