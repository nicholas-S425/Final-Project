import {useState, useEffect} from 'react';
import axios from 'axios';
function StatsCounter({list}) {
  return (
    <div style={{padding: '10px', border: '1px solid black', display: 'inline-block', margin: '10px'}}>
     <p>Total Accounts: {list.length}</p>
    </div>
  );
}
function App() {
  const [name, setName] = useState("");
  const [password, setPassword] = useState(""); 
  const [email, setEmail] = useState(""); 
  const [list, setList] = useState([]);
const handleAdd = async () => {
  if (!name.trim()) return;
  try {const res = await axios.post('http://localhost:5000/api/items', {
      name,
      email,
      password
    });
    setList([...list, res.data]);
    setName("");
    setEmail("");
    setPassword("");
  } catch (err) {
    console.log(err);
  }
};
useEffect(() => {
  axios.get('http://localhost:5000/api/items')
    .then(res =>setList(res.data))
    .catch(err =>console.log(err));
}, []);
const handleDelete = async (id) => {
  console.log("Deleting id:", id);
  try {
    await axios.delete(`http://localhost:5000/api/items/${id}`);
    setList(list.filter(item => item._id !== id));
  } catch (err) {
    console.log("Delete error:", err);
  }
};

  return (
    <>
      <h1>Account: </h1>
      <StatsCounter list={list} />
      
      <div style={{padding:'5px'}}>
      </div>
        <div style={{padding: '10px'}}>
        <p1>Name: </p1>
        <input style={{padding:'2px'}} type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Name" 
        />
        </div>
        <div style={{padding:'10px'}}>
        <p1>Email: </p1>
        <input style={{padding:'2px'}} type ="text"//type="email" //autoComplete="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Email" 
        />
        </div>

        <div style={{padding: '10px'}}>
        <p1>Password: </p1>
        <input style={{padding:'2px'}} type="text"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Password" 
        />
        </div>
        <div style={{padding: '10px'}}>
        <button id="hover" onClick={handleAdd}>Create Account</button>
        <ol>
        {list.map((item, index) => (
          <div key={index}>
            <img id="icon" src="/d6cdf2a5daaf96462127cc31fb621851-removebg-preview.png"/>
            <li>Account: {item.name} Email: {item.email} Password: {item.password}</li>
            <button onClick={() => handleDelete(item._id)}>Delete</button>
            
          </div>
        ))}
        </ol>
        </div>
        
    </>
  );
}


export default App;