# Packer Demo

## 1 Packer Basics:

### 1.1 Packer Configuration file

Main Configuration in JSON (example):
```
{
    "variables": {
        "variable1": "default value",
        "variable2": "default value"
    },
    "builders": {
        [
            {
                "type": "builder-type",
                ...
            }
        ]
    },
    "post-processors": [
        [
            {
                "type": "post-processor type",
                ...
            }
        ]
    ]
}
```

### 1.2 Packer Commands
```
# Build Image
$ packer build << packer_template.json >>

# Build Image with Custom Variables
$ packer build -var variable1=some_value << packer_template.json >>
$ packer build -var-file=file_with_vars << packer_template.json >>

# Restrict Builders (builder names/types: foo, bar, baz)
$ packer build -only=foo,bar,baz << packer_template.json >>

# Validate Template
$ packer validate << packer_template.json >>
```

### 1.3 More Details:
- [Installing Packer](https://www.packer.io/intro/getting-started/install.html)
- [Variables](https://www.packer.io/docs/templates/user-variables.html)
- [Template Builders](https://www.packer.io/docs/templates/builders.html)
- [Template Post-Processors](https://www.packer.io/docs/templates/post-processors.html)
- [Builder: `docker`](https://www.packer.io/docs/builders/docker.html)
- [Provisioner: `shell`](https://www.packer.io/docs/provisioners/shell.html)
- [Post-Processor: `docker-tag`](https://www.packer.io/docs/post-processors/docker-tag.html)
- [Post-Processor: `docker-push`](https://www.packer.io/docs/post-processors/docker-push.html)

## 2 Project Structure

Packer Configuration: [example.json](example.json)
Ansible Playbook: [playbook.yml](playbook.yml)
Asnible Roles: [roles/nginx](roles/nginx)

## 3 Building Image

```
$ packer build example.json
```

## 4 Spinning Up a Container from the Image

```
$ docker run -d --privileged -P 80:80 centos-built-by-packer-with-ansible:2018-11-05-11-53-34
```