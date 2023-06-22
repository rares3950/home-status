# Home-Status
Home-Status is a web application written in Python that helps you monitor your homelab's uptime from a dead simple web interface
![the interface](https://i.imgur.com/mJsqTEE.png)

## Deployment
### Standalone 
This considers that you have already installed Python and Python VirtualEnv

Firstly, you're going to have to clone the repository. This is trivially easy
```sh
git clone https://github.com/rares3950/home-status.git
cd home-status
```

Now, you'll need to create a virtual enviorment and install the required dependencies.
```sh
python -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

After you've done this, you can now configure servers.yaml. This should be trivially easy.
```sh
cp servers.yaml.example servers.yaml
nano servers.yaml
```
For example
```yaml
servers:
  openmediavault:
    hostname: "openmediavault"
    localip: 192.168.1.10
```

Now, it's time to run the server. In order to check that everything works fine, I reccomend running `flask run`. Do not use this in production. If everything works fine, you can now deploy it in production.

Please audit the `homestatus.service` file in order to work for your installation. After you have audited the file, configure the service to work.
```sh
sudo cp ./homestatus.service /etc/systemd/system/homestatus.service
sudo systemctl daemon-reload
sudo systemctl enable --now homestatus
```

Your homestatus service is now listening on port 2020, or whatever port you have chosen.

### Docker (soon!)