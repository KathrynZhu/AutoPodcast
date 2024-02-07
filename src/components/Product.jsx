import './Product.css';

const formatPrice = new Intl.NumberFormat([], { style: 'currency', currency: 'USD' }).format;

const Product = ({product}) => (
  <div className="card m-1 p-2">
    <img src={product.thumbnail} className="card-img-top" alt={product.description} />
    <div className="card-body">
      <h5 className="card-title">{product.title}</h5>
      <p className="card-text">{product.title}</p>
      <p className="card-text">{formatPrice(product.price)}</p>
    </div>
  </div>
);

export default Product;