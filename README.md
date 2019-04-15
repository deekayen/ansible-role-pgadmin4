pgAdmin4
========

[![Build Status](https://travis-ci.org/deekayen/ansible-role-pgadmin4.svg?branch=master)](https://travis-ci.org/deekayen/ansible-role-pgadmin4)

Install pgAdmin4 web client and client binaries.

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

    - hosts: servers
      roles:
         - deekayen.pgadmin4


Author Information
------------------

Most of the work was done by Tadej Borovšak in [Installing pgAdmin4 on Centos 7](https://tech.xlab.si/posts/installing-pgadmin4-on-centos-7/).
