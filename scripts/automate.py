import subprocess
import os

# Get the current working directory and construct paths to playbooks and inventory
current_directory = os.path.dirname(os.path.abspath(__file__))
webserver_playbook = os.path.join(current_directory, '../ansible/webserver.yml')
dbserver_playbook = os.path.join(current_directory, '../ansible/dbserver.yml')
inventory = os.path.join(current_directory, '../ansible/inventory.ini')

def run_playbook(playbook):
    try:
        # Execute the ansible-playbook command with the inventory file
        result = subprocess.run(['ansible-playbook', '-i', inventory, playbook], check=True, stdout=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

# Trigger web server and database playbooks
run_playbook(webserver_playbook)
run_playbook(dbserver_playbook)
