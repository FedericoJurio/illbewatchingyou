<p align="center">
  <img src="https://github.com/FedericoJurio/illbewatchingyou/blob/master/static/rat.png?raw=true" alt="Logo" width="128" height="128">
</p>
<h3 align="center">I'll be watching you</h3>
<p align="center">Watch product availability in MercadoLibre</p>

## About the project
I'll be watching you provides a periodic task to verify the availability of products in MercadoLibre and sends a message through Telegram when there's stock.

## Motivation
A few days ago I had to buy an oven, I did market research and the best price was provided by the manufacturer that sells their products through their official store hosted by MercadoLibre, the biggest eCommerce platform in Argentina.

For those who don't live in Argentina, it's pretty common to find different prices for the same product, there are several factors that make this happen, but the root cause is the country's inflation.

I didn't buy the product because it was late. Big mistake. The next day in the morning I was ready to do it but it wasn't available anymore. I sent a message to the manufacturer and they told me that they will have stock again in a couple of days so I promised myself to buy the product right after it became available.

## Getting started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Docker
- Docker-Compose
- Telegram Bot

### Running the application
1. Clone this repository `git@github.com:FedericoJurio/illbewatchingyou.git`
1. Access to the project directory `cd illbewatchingyou`
1. Update the `products.yaml` file by adding the products of your interest
1. Update the `.env` file by adding the Telegram chat identifier, username, and password
1. Build the containers `docker-compose build`
1. Run the application `docker-compose up`

## License
Distributed under the MIT License. See `LICENSE` for more information.
