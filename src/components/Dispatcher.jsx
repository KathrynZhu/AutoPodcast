import { BrowserRouter, Routes, Route } from "react-router-dom";
import Posts from './Posts';
import Users from './Users';

const Dispatcher = ({users, posts}) => (
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<Posts posts={posts} users={users} />} />
      <Route path="/users" element={<Users users={users} />} />
    </Routes>
  </BrowserRouter>
);

export default Dispatcher;