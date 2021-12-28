import smtplib
import renderer

YOUR_SMTP_ADDRESS = "smtp.gmail.com"
YOUR_EMAIL = "example.com"
YOUR_PASSWORD = "12345678"


class Smtp:
    def __init__(self):
        self.buy_price = 200

    def calculate_condition(self):
        render_a_page = renderer.Renderer()
        soup = render_a_page.get_soup()

        title = soup.find(id="productTitle").get_text().strip()
        print(title)

        price_as_float = render_a_page.find_price()

        if price_as_float < self.buy_price:
            message = f"{title} is now {price_as_float}"

            with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
                connection.starttls()
                result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
                connection.sendmail(
                    from_addr=YOUR_EMAIL,
                    to_addrs=YOUR_EMAIL,
                    msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
                )
