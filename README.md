# Product Search Project

This project is a web application built with Django that allows users to search for products on Amazon and Temu using their respective RapidAPI services.

**Important:** This project requires API keys from RapidAPI. You will need to subscribe to the following services and replace the placeholder `YOUR-API-KEY` in the `views.py` file with your actual keys:

*   [Real-Time Amazon Data API](YOUR_AMAZON_API_LINK) (replace with the actual link)
*   [Temu.com Shopping API (Unofficial)](YOUR_TEMU_API_LINK) (replace with the actual link)

## Features

*   Search for products on Amazon and Temu.
*   View product listings with title, price, image, and source website.
*   Results are sorted by price (ascending).
*   Uses caching to improve performance and reduce API calls.
*   Stylish user interface.

## Getting Started

These instructions will guide you on how to get a copy of the project up and running on your local machine.

### Prerequisites

*   Python 3.7 or higher
*   pip (Python package installer)
*   Git
*   A RapidAPI account with subscriptions to the APIs listed above.

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/product-search.git
    cd product-search
    ```

2. **Install dependencies:**

    This project uses the following external libraries:

    *   **Django:** `pip install django`
    *   **Requests:** `pip install requests`
    *   **urllib (built-in):** (No installation needed)

    You will need to install these libraries manually using `pip`.

3. **Set up API keys:**

    *   Open the `products/views.py` file.
    *   Replace `YOUR-API-KEY` in the `get_amazon_products` and `get_temu_products` functions with your actual RapidAPI keys for Amazon and Temu, respectively.

4. **Run the Django development server:**

    ```bash
    python manage.py runserver
    ```

5. **Access the application:**

    *   Open your web browser and go to `http://127.0.0.1:8000/`.

## Adding Other Websites

This project is designed to be easily extensible. To add other websites:

1. **Find a suitable RapidAPI service** for the website you want to add.
2. **Create a new function** in `views.py` (similar to `get_amazon_products` and `get_temu_products`) to handle fetching data from that website's API.
3. **Update the `product_search` function** in `views.py` to include the new website in the search process.
4. **Modify the `search.html` template** to add the new website as an option in the checkboxes.
5. **Adjust the `product_search.html` template** if necessary to display product information specific to the new website.

**Important:** Everyone who downloads and uses this project will need to:

*   **Subscribe to the required RapidAPI services** and obtain their own API keys.
*   **Replace the placeholder API keys** in the `views.py` file with their actual keys.

## Contributing

(Add guidelines for contributing if you want to accept contributions.)

## License

(Choose a license for your project and add the license information here.)

## Acknowledgments

*   This project uses the [RapidAPI](https://rapidapi.com/) platform to access Amazon and Temu product data.