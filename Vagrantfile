VAGRANTFILE_API_VERSION = '2'

Vagrant.configure(2) do |config|
    config.vm.box = "ubuntu/xenial64"
    config.vm.box_version = "20180323.0.0" 
    config.vm.network "forwarded_port", guest:80, host:42069
    config.vm.hostname = "hh-backend-dev"
    config.vm.provision :docker
    config.vm.provision :docker_compose, yml: "/vagrant/docker-compose.yml", run:"always"
end
