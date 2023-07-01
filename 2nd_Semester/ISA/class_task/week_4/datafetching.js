
// !
const products = [
    {
        id: 1,
        name: 'Basic Tee',
        href: '#',
        imageSrc:
            'https://tailwindui.com/img/ecommerce-images/product-page-01-related-product-01.jpg',
        imageAlt: "Front of men's Basic Tee in black.",
        price: '$35',
        color: 'Black',
    },
    {
        id: 2,
        name: 'Basic Tee',
        href: '#',
        imageSrc:
            'https://tailwindui.com/img/ecommerce-images/product-page-01-related-product-01.jpg',
        imageAlt: "Front of men's Basic Tee in black.",
        price: '$35',
        color: 'Black',
    },
    {
        id: 3,
        name: 'Basic Tee',
        href: '#',
        imageSrc:
            'https://tailwindui.com/img/ecommerce-images/product-page-01-related-product-01.jpg',
        imageAlt: "Front of men's Basic Tee in black.",
        price: '$35',
        color: 'Black',
    },
];
const div = document.querySelector('#products')
products.forEach((product) => {
    const productDiv = document.createElement('div');
    productDiv.innerHTML = `
      <a href="${product.href}">
        <img src="${product.imageSrc}" alt="${product.imageAlt}">
        <h3>${product.name}</h3>
        <p>${product.price}</p>
        <p>${product.color}</p>
      </a>
    `;

    div.appendChild(productDiv);
});











//!
//! Template Literals: You can write use html variables in your string message.
// const productTemplate = {
//     id: 1,
//     name: 'Basic Tee',
//     href: '#',
//     imageSrc:
//         'https://tailwindui.com/img/ecommerce-images/product-page-01-related-product-01.jpg',
//     imageAlt: "Front of men's Basic Tee in black.",
//     price: '$35',
//     color: 'Black',
// }

// const div = document.querySelector('#products')

// const message = `Hello ${productTemplate.name}, You have to pay ${productTemplate.price}.`

// div.innerHTML = message;








