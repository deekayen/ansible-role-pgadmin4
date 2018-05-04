pgAdmin4
========

Install pgAdmin4 web client.

Default Variables
-----------------

```
pgdg_package: https://download.postgresql.org/pub/repos/yum/10/redhat/rhel-7-x86_64/pgdg-redhat10-10-2.noarch.rpm
pgadmin_setup_email: admin@example.com
pgadmin_setup_password: correct horse battery staple
```

Dependencies
------------

The EPEL repo is used to get dependencies.

 * geerlingguy.repo-epel

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: deekayen.pgadmin4 }


Author Information
------------------

Most of the work was done Tadej Borovšak in [Installing pgAdmin4 on Centos 7](https://tech.xlab.si/posts/installing-pgadmin4-on-centos-7/).
