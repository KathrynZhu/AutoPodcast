const UserContact = ({user}) => (
    <table className="table table-bordered">
      <tbody>
        <tr><th style={{width: '7em'}}>Name</th><td>{user.firstName} {user.lastName}</td></tr>
        <tr><th>Email</th><td>{user.email}</td></tr>
        <tr><th>Phone</th><td>{user.phone}</td></tr>
        <tr>
          <th>Address</th>
          <td>
            {user.address.address}, {user.address.city}, {user.address.state} {user.address.postalCode}
          </td>
        </tr>
      </tbody>
    </table>
  );
  
  export default UserContact;