import React from 'react';
import './App.css';

function fetchData(){
  return fetch("http://127.0.0.1:5000/")
  .then(function(response){
    if (response.ok) {
      //recebe a resposta
      let responseType = response.headers.get('content-type');
      if (responseType && responseType.indexOf("application/json") !== 1) {
          return response.json().then(function(json){
            return json;
        });
      }

    }else{
      console.log("Ocorreu um erro.");
      return {error: "Status not ok."};
    }
  })
  .catch(function(error){
    console.log("Ocorreu um erro na operacao fetch: " + error.message);
    return {error: "Failed to connect."};
  });
}


class ItensForm extends React.Component{
  constructor(props){
    super(props);
    this.state = {itens_list : null}
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
}

handleChange(event){
    this.setState({inputText: event.target.value});   
}

  handleSubmit(event){
      event.preventDefault();
      //this.setState({loading: true});
      fetchData().then(response => this.setState({itens_list: response}));
  }

  render(){
    return (
      <div>
        <h1>Mareloja</h1>
        <div className='itens'>
          <form onSubmit={this.handleSubmit}>
            {this.state.itens_list}
            Nome - R$15 - Disponível: 10 
            <button value={"Comprar"} class="button" type="submit">Comprar</button>
          </form>
        </div>
      </div>
    );
  }

}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <ItensForm></ItensForm>
      </header>
    </div>
  );
}

export default App;
