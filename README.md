pgAdmin4
========

[![CI](https://github.com/deekayen/ansible-role-pgadmin4/actions/workflows/ci.yml/badge.svg)](https://github.com/deekayen/ansible-role-pgadmin4/actions/workflows/ci.yml) [![Project Status: Inactive – The project has reached a stable, usable state but is no longer being actively developed; support/maintenance will be provided as time allows.](https://www.repostatus.org/badges/latest/inactive.svg)](https://www.repostatus.org/#inactive)

Install pgAdmin4 web client and client binaries.

Default Variables
-----------------

```
pgadmin_setup_email: admin@example.com
pgadmin_setup_password: correct horse battery staple
```

Static Variables
----------------

```
pgdg_key: https://download.postgresql.org/pub/repos/yum/RPM-GPG-KEY-PGDG
pgdg_package: "https://download.postgresql.org/pub/repos/yum/reporpms/EL-{{ ansible_distribution_major_version }}-x86_64/pgdg-redhat-repo-latest.noarch.rpm"

pgadmin_key: https://keys.openpgp.org/vks/v1/by-fingerprint/E8697E2EEF76C02D3A6332778881B2A8210976F2
pgadmin_package: https://ftp.postgresql.org/pub/pgadmin/pgadmin4/yum/pgadmin4-redhat-repo-2-1.noarch.rpm
```

Dependencies
------------

The EPEL repo is used to get python dependencies.

 * geerlingguy.repo-epel

Example Playbook
----------------

    - hosts: servers
      roles:
         - deekayen.pgadmin4


Author Information
------------------

Most of the work was done by Tadej Borovšak in [Installing pgAdmin4 on Centos 7](https://tech.xlab.si/posts/installing-pgadmin4-on-centos-7/).
