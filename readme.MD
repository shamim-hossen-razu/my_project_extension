# 'my_project_extension' Installation guide

This instruction manual assumes that you already have odoo 16 running on a linux machine
And you want to add this module to your custom addons

## Step 1:
Activate virtual environments and Install Web and package Dependencies if not satisfied by the system

```sudo apt install python3-pip libldap2-dev libpq-dev libsasl2-dev```

``` pip install -r requirements.txt ```
## Step 2: update conf file 
Add this module to the custom-addons directory

## Step 3: odoo service and update apps list
activate developer mode and go to apps , Click on update apps list

## Step 4: Install my_project_extension
Search for my_project_extension and activate / install it

## Step 5: log in with user who has admin privileges on project module to access Team 
Set up team with team member and project to achieve feature like project will only be visible to team members

## Step 6: Access Dashboard 
From project menu access Dashboard menu . apply filter and see result as task count

