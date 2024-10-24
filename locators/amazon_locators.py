class AmazonLocators:
    ALLOW_NOTIFICATIONS_BTN = 'com.android.permissioncontroller:id/permission_allow_button'
    SKIP_SIGN_IN_BTN = 'com.amazon.mShop.android.shopping:id/skip_sign_in_button'
    DISMISS_BTN = 'com.amazon.mShop.android.shopping:id/left_button'
    LAPTOP_MENU = '//android.widget.Image[@text="Laptops"]'
    PRODUCT_NAME_BOX = '//android.webkit.WebView[@text="Amazon.com : laptops"]/android.view.View/android.view.View/android.view.View[4]/android.view.View'
    EXPECTED_PRODUCT_NAME = 'ASUS 15.6” Vivobook Go Laptop, Intel Celeron N4500, 4GB RAM, 128GB SSD, Windows 11 in S Mode, Star Black, L510KA-ES04'
    ADD_TO_CART_BTN = '(//android.widget.Button[@text="Add to cart"])[2]'
    SEARCH_BOX = '//android.widget.TextView[@resource-id="com.amazon.mShop.android.shopping:id/chrome_search_hint_view"]'
    SEARCH_BOX_ENABLED = '//android.widget.EditText[@resource-id="com.amazon.mShop.android.shopping:id/rs_search_src_text"]'
    HOT_WHEELS_STORE = '//android.widget.Button[@text="Shop the Hot Wheels store"]'
    NAVBAR_PHARMACY_BTN = '//android.widget.TextView[@resource-id="com.amazon.mShop.android.shopping:id/subnav_button_text" and @text="Pharmacy"]'
    EXPLORE_ALL_THE_WAYS_TO_SAVE_BTN = '//android.widget.TextView[@text="Explore all the ways to save"]'
    SEARCH_FOR_MEDICATION_FIELD = '//android.widget.EditText'
    BROWSER_MENU_BTN = '//android.widget.ImageView[@content-desc="Browse menu Tab 5 of 5"]'

    # Browser menu buttons
    AUTOMOTIVE_BTN = '(//android.view.ViewGroup[@resource-id="theme_card_content_view_test_id"])[13]'
    PRIME_BTN = '(//android.view.ViewGroup[@resource-id="theme_card_content_view_test_id"])[1]'
    AUTOMOTIVE_PARTS_ACCESSORIES = '//android.view.View[@resource-id="sbdau"]'

    # Automotive buttons
    ADD_A_NEW_VEHICLE_BTN = '//android.widget.Button[@text="Add a new vehicle"]'
    SELECT_A_VEHICLE_TYPE_BTN = '(//android.view.View[@text="Select a Vehicle Type"])[1]'
    CARS_AND_TRUCKS_BTN = '//android.view.View[@text="Cars & Trucks"]'
    AMAZON_AUTOMOTIVE_BANNER = '//android.widget.Image[@text="Amazon Automotive"]'
    MANAGE_YOUR_GARAGE_BTN = '//android.widget.TextView[@text="Manage Your Garage"]'
