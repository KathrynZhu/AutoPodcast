import { Link } from 'react-router-dom';
import { firstLastName } from "./User";

const Posts = ({ posts, users }) => (
  <>
    {
      Object.entries(posts).map(([key, post]) => (
        <div key={`post-${key}`}>
          <h3>{post.title}</h3>
          <p>{post.body}</p>
          <p> -- <Link to={`/users/${post.userId}`}>{firstLastName(users[post.userId])}</Link></p>
        </div>
      ))
    }
  </>
);

export default Posts;