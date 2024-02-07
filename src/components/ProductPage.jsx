/*import { useState } from 'react';
import Modal from './Modal';
import ProductList from './ProductList';

const ProductPage = () => {
  const [selected, setSelected] = useState([]);
  const [open, setOpen] = useState(false);

  const openModal = () => setOpen(true);
  const closeModal = () => setOpen(false);
  //...
  return (
    <div>
      <button className="btn btn-outline-dark" onClick={openModal}><i className="bi bi-cart4"></i></button>
      <Modal open={open} close={closeModal}>
        <Cart selected={selected} />
      </Modal>
      <ProductList products={data.products} selected={selected} toggleSelected={toggleSelected} />
    </div>
  );
};*/

import { useState } from 'react';
import ProductList from "./ProductList";

const ProductPage = ({products}) => {
  const [selected, setSelected] = useState([]);

  const toggleSelected = (item) => setSelected(
    selected.includes(item)
    ? selected.filter(x => x !== item)
    : [...selected, item]
  );

  return (
    <ProductList products={products} selected={selected} toggleSelected={toggleSelected} />
  );
};

export default ProductPage;