import UserContact from './UserContact';
          
const UserContacts = ({users}) => (
  <div>
    { Object.entries(users).map(([id, user]) => <UserContact key={id} user={user} />) }
  </div>
);

export default UserContacts;