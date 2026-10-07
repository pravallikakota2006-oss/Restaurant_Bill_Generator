import streamlit as st

# Page settings
st.set_page_config(
    page_title="Pravallika's Restaurant",
    page_icon="🍔",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

.main {
    background: linear-gradient(135deg, #fff7ed, #fef2f2);
}

.block-container {
    max-width: 900px;
    padding-top: 2rem;
}

.hero {
    padding: 25px;
    border-radius: 22px;
    background: linear-gradient(135deg, #ff7a18, #ff3d68);
    color: white;
    text-align: center;
    box-shadow: 0 10px 25px rgba(0,0,0,0.12);
}

.card {
    padding: 18px;
    border-radius: 18px;
    background: white;
    box-shadow: 0 4px 18px rgba(0,0,0,0.08);
    margin: 10px 0;
}

</style>
""", unsafe_allow_html=True)


# Header
st.markdown("""
<div class="hero">

<h1>🍔 Pravallika's Restaurant</h1>

<p>Simple • Smart • Delicious Bill Generator</p>

</div>
""", unsafe_allow_html=True)


# Food menu
menu = {
    "🍕 Margherita Pizza": 249,
    "🍔 Veg Burger": 149,
    "🍝 White Sauce Pasta": 199,
    "🥪 Club Sandwich": 129,
    "🍟 French Fries": 99,
    "🥤 Cold Drink": 59,
    "🍰 Chocolate Cake": 119
}


# Food selection
st.subheader("🛒 Select your items")

items = {}

cols = st.columns(2)

for i, (item, price) in enumerate(menu.items()):

    with cols[i % 2]:

        quantity = st.number_input(
            f"{item} — ₹{price}",
            min_value=0,
            max_value=20,
            value=0,
            step=1,
            key=item
        )

        if quantity > 0:
            items[item] = (price, quantity)


# Discount and tax
st.divider()

col1, col2 = st.columns(2)

with col1:

    discount = st.number_input(
        "🏷️ Discount (%)",
        min_value=0.0,
        max_value=50.0,
        value=0.0,
        step=1.0
    )

with col2:

    tax = st.number_input(
        "🧾 Tax (%)",
        min_value=0.0,
        max_value=30.0,
        value=5.0,
        step=0.5
    )


# Generate bill
if st.button(
    "✨ Generate Final Bill",
    type="primary",
    use_container_width=True
):

    if not items:

        st.warning(
            "Please select at least one food item."
        )

    else:

        # Calculate subtotal
        subtotal = sum(
            price * quantity
            for price, quantity in items.values()
        )

        # Calculate discount
        discount_amount = (
            subtotal * discount / 100
        )

        # Amount after discount
        taxable_amount = (
            subtotal - discount_amount
        )

        # Calculate tax
        tax_amount = (
            taxable_amount * tax / 100
        )

        # Final total
        total = (
            taxable_amount + tax_amount
        )


        # Success message
        st.success(
            "Bill generated successfully!"
        )


        # Bill
        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )

        st.subheader("🧾 Final Bill")


        # Display selected items
        for item, (price, quantity) in items.items():

            item_total = price * quantity

            st.write(
                f"**{item}** × {quantity} — "
                f"₹{item_total:,.2f}"
            )


        st.divider()


        # Display calculations
        st.write(
            f"Subtotal: **₹{subtotal:,.2f}**"
        )

        st.write(
            f"Discount: **− ₹{discount_amount:,.2f}**"
        )

        st.write(
            f"Tax: **+ ₹{tax_amount:,.2f}**"
        )


        st.markdown(
            f"### 💰 Grand Total: ₹{total:,.2f}"
        )


        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


# Footer
st.caption(
    "Created by Pravallika • "
    "Python + Streamlit Project Challenge"
)