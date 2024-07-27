import {Button} from '@nextui-org/button';


export default function Dashboad() {
  return (
    <div className="grid grid-flow-col bg-orange-200">
      <div className="col-span-3 bg-slate-100">

      <Button color="default">
        Default gggg
      </Button>
      <Button color="primary">
        Primary
      </Button>  
      <Button color="secondary">
        Secondary
      </Button>  
      <Button color="success">
        Success
      </Button>  
      <Button color="warning">
        Warning
      </Button>  
      <Button color="danger">
        Danger
      </Button>  

        
        <p className="text-red-500">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Dolorum neque iusto debitis obcaecati iste. Laboriosam deserunt doloremque sit cumque, veritatis tempora harum? Dolorum sint, reiciendi.</p>
      </div>
      <div className="col-span-9 bg-green-100">
        <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Dolorum neque iusto debitis obcaecati iste. Laboriosam deserunt doloremque sit cumque, veritatis tempora harum? Dolorum sint, reiciendi.</p>
      </div>
      
      
    </div>
    
  );
}
