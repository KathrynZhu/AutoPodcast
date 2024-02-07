import './ProductList.css';
import Product from './Product';
import './Products.css'

const ProductList = ({products}) => (
  <div className="product-list">
    {
      products.map(product => <Product key={product.id} product={product} />)
    }
  </div>
);