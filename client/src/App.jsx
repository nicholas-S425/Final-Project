import { useEffect, useState } from 'react'

function App() {
  const [greeting, setGreeting] = useState("Loading...")

  useEffect(() => {
    fetch('http://localhost:5000/api/hello')
      .then(res => res.json())
      .then(data => setGreeting(data.message))
      .catch(err => setGreeting("Server is not responding 😢"))
  }, [])

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>MERN Stack Test</h1>
      <p>Message from Backend: <strong>{greeting}</strong></p>
    </div>
  )
}
export default App
