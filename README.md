# getserv
![Build status](https://img.shields.io/github/workflow/status/davideperozzi/getserv/%5BDeploy%5D%20Build%20and%20deploy?style=flat-square)
[![License](https://flat.badgen.net/badge/license/MIT/blue)](./LICENSE)

This tool is used to retrieve stable servers from various services.

## Usage
The package is uploaded to [pypi.org](https://pypi.org/project/getserv/). In order to install the package you should use pip:
```
pip install getserv
```
> python >= 3.6 is required

## Basic usage
Basically the driver is responsible for delivering the ips to the main program. The main program will just scan all the ips received from the driver and checks whether a service on a given port is available:
```sh
getserv [...args] {driver_name} [...args]
```

### Changing the port to scan
The default port is `22`. You may change it with the `--test-port` (`-p`) option.

### Listing all IPs
The default beheavior is to only return one address. You can list all available server IPs by adding the `--list-all` (`-a`) option.

## The DigitalOcean driver
The digitalocean driver is used to filter droplets by multiple tags. Since the `doctl` can only filter by single tags, the driver will fallback to the REST API. It'll get information for the requested droplets and filters by the given tags. In order to get a running droplet from your droplet stack you execute this:

```sh
getserv digitalocean tag1,tag2
```

To authenticate yourself you can use either a cli argument or a environemt variable:

```sh
getserv digitalocean \
  --digitalocean-access-token XXXXXXXXXXX \
  tag1,tag2
```

Or to use the environment varible:
```sh
export DIGITALOCEAN_ACCESS_TOKEN=XXXXXXXX
getserv digitalocean tag1,tag2
```

> If everything is configured properly you should receive a single IP based on the availability of your droplets

## License
See the [LICENSE](./LICENSE) file for license rights and limitations (MIT).
