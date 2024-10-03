import subprocess

def run_playbook(playbook):
    try:
        # Execute the ansible playbook command
        result = subprocess.run(['ansible-playbook', playbook], check=True, stdout=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

# Trigger web server and database playbooks
run_playbook('webserver.yml')
run_playbook('dbserver.yml')
