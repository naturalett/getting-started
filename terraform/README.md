<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#Install-Terraform">Install Terraform</a></li>
    <li><a href="#roadmap">Google an example</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#clone">clone</a></li>
        <li><a href="#initialize">Installation</a></li>
        <li><a href="#plan">plan</a></li>
        <li><a href="#apply">apply</a></li>
        <li><a href="#destroy">destroy</a></li>
      </ul>
    </li>
    <li><a href="#Usage">Usage</a></li>
  </ol>
</details>


<!-- Install Terraform -->
## Install Terraform

#### The link below provides instruction of how to install Terraform

```BASH
https://learn.hashicorp.com/tutorials/terraform/install-cli
```


<!-- Google an example -->
## Google an example

#### Let's google an example of how to create a docker image

```BASH
https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs/resources/image
```


<!-- GETTING STARTED -->
## Getting Started

#### An example of a docker_image resource

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
