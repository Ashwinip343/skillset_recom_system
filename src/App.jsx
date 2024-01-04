import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Roles from './sample.json'

import fields from './field_wise.json'
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
     <div className='container'>
      {Roles.map(role=>{
        return (
          <>
         <div className='box'>{role.role}</div>
         <div className='hey'>{role.content}</div>
          </>
        )
      })}
     </div>
    </>
  )
}

export default App
