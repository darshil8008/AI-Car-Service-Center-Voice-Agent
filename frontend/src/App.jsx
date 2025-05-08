import { useState } from 'react'
import './App.css'
import LiveKitModal from './components/LiveKitModal';

function App() {
  const [showSupport, setShowSupport] = useState(false);

  const handleSupportClick = () => {
    setShowSupport(true)
  }

  return (
    <div className="app">
      <header className="header">
        <div className="logo">CarsHelp.com</div>
      </header>

      <main>
        <section className="hero">
          <h1>Smarter Car Help Starts Here</h1>
          <p>Real-Time Vehicle Help, Powered by AI — Anytime, Anywhere.</p>
            <div className="search-bar">
            <input type="text" placeholder='Enter vehicle or part number'></input>
            <button>Search</button>
          </div>
        </section>

        <button className="support-button" onClick={handleSupportClick}>
          Talk to an Agent!
        </button>
      </main>

      {showSupport && <LiveKitModal setShowSupport={setShowSupport}/>}
    </div>
  )
}

export default App
