/*import { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-icons/font/bootstrap-icons.css';
import './App.css';
//import ProductList from './components/ProductList';
const App = () => {
  const [count, setCount] = useState(0);
  const today = new Date();
  const day = today.toLocaleString([], {weekday: 'long'});
  const date = today.toLocaleDateString([], {dateStyle: 'long'})
  return (
    <div className="container">
      <p>podcastpage</p>
      <h1>This should be the homepage</h1>
      
      <p>Today is {day}, {date}.</p>
    </div>
  );
};

export default App;
*/
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { useJsonQuery } from './utilities/fetch';

const Main = () => {
  const [data, isLoading, error] = useJsonQuery('https://dummyjson.com/users');

  if (error) return <h1>Error loading user data: {`${error}`}</h1>;
  if (isLoading) return <h1>Loading user data...</h1>;
  if (!data) return <h1>No user data found</h1>;

  return data.users.map(user => <div key={user.id}>{user.firstName} {user.lastName}</div>);
}

const queryClient = new QueryClient();

const App = () => (
  <QueryClientProvider client={queryClient}>
    <div className="container">
      <Main />
    </div>
  </QueryClientProvider>
);

export default App;
/*
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { useJsonQueries } from './utilities/fetch';

const Main = () => {
  const [data, isLoading, error] = useJsonQueries({
    userData: 'https://dummyjson.com/users',
    postData: 'https://dummyjson.com/posts'
  });

  if (error) return <h1>Error loading data: {`${error}`}</h1>;
  if (isLoading) return <h1>Loading data...</h1>;
  if (!data) return <h1>No data found</h1>;

  const users = data.userData.users;
  const posts = data.postData.posts;

  return posts.map((post) => {
    const user = users.find(user => user.id === post.userId);
    const author = user ? `${user.firstName} ${user.lastName}` : 'Unknown author';
    return  <div key={post.id}>{post.title} -- {author}</div>;
  });
};

const queryClient = new QueryClient();

const PostApp = () => (
  <QueryClientProvider client={queryClient}>
    <div className="container">
      <Main />
    </div>
  </QueryClientProvider>
);

export default PostApp;*/
