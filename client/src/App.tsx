import React from 'react';
import history from './history'
import {Router,Route} from 'react-router-dom'
import Home from './components/Home'
import {ChakraProvider} from '@chakra-ui/react'
function App() {
  return (
    <ChakraProvider>
      <Router history={history}>
        <Route path="/" component={Home} />
      </Router>
    </ChakraProvider>
  );
}

export default App;
