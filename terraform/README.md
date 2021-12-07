## The link below provides instruction of how to install Terraform

```BASH
https://learn.hashicorp.com/tutorials/terraform/install-cli
```

## Let's google an example of how to create a docker image

```BASH
https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs/resources/image
```

### An example of a docker_image resource

1. Clone the repo
   ```sh
   git clone git@github.com:naturalett/getting-started.git
   ```
3. Initialize a working directory for Terraform configuration files
   ```sh
   terraform init
   ```
4. Evaluates a Terraform configuration to determine the desired state of all the resources it declares
   ```sh
   terraform plan
   ```
5. Makes any infrastructure changes defined in your configuration
   ```sh
   terraform apply
   ```
6. Destroy all your created infrastructure in your configuration
   ```sh
   terraform destroy
   ```

<!-- USAGE EXAMPLES -->
## Usage

- [x] Check the created image
   ```sh
   docker image ls | grep ubuntu
   ```
