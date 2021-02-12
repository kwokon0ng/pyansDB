## ansible vault to encrypt yml playbook file

ansible-vault encrypt  first-playbook.yml --ask-vault-pass

# to run
ansible-playbook first-playbook.yml --ask-vault-pass

ansible-vault decrypt  first-playbook.yml --ask-vault-pass
