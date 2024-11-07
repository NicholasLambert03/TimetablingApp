import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Homepage from '../pages/Homepage'
import Edit from '../pages/Edit'

function AppRouter() {

  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element = {<Homepage/>}/>
        <Route path='/edit' element = {<Edit/>}/>
      </Routes>
    </BrowserRouter>
  )
}

export default AppRouter
