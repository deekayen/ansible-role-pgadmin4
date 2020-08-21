import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_awscli2_apache(host):
    assert host.package("httpd").is_installed
    assert host.package("mod_wsgi").is_installed

    assert host.file("/etc/httpd/conf.d/pgadmin4.conf").is_file

    assert host.service('httpd').is_enabled
    assert host.service('httpd').is_running

    assert host.user("apache").exists


def test_awscli2_pyenv(host):
    assert host.package("python-alembic").is_installed
    assert host.package("python-flask").is_installed
    assert host.package("python-psycopg2").is_installed


def test_awscli2_pgadmin4(host):
    assert host.package("pgadmin4-web").is_installed
    assert host.package("postgresql11").is_installed

    assert host.file("/var/lib/pgadmin/pgadmin4.db").is_file

    assert host.file("/var/log/pgadmin").is_directory
    assert host.file("/var/lib/pgadmin").is_directory
