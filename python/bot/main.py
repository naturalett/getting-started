import renderer


def main():
    render_a_page = renderer.Renderer()
    amazon_product_price = render_a_page.find_price()

    soup = render_a_page.get_soup()
    title = soup.find(id="productTitle").get_text().strip()
    print(title)
    print(amazon_product_price)


if __name__ == '__main__':
    main()
