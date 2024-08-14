/* eslint-disable prettier/prettier */
import React from "react";

import FormTeste from "./form-teste";

import PgMenuLateralLayout from "@/components/PgMenuLateralLayout";
import CpHeaderMain from "@/components/CpHeaderMain";
import CpMenulateral from "@/components/CpMenuLateral";
import CpFooter from "@/components/CpFooter";
import CpFormTeste from "@/components/CpFormTeste";



export default function Teste() {
  return (
    <PgMenuLateralLayout
      footer={<CpFooter />} 
      header={<CpHeaderMain />}
      menu={ <CpMenulateral/> }
    >
      <FormTeste />
    </PgMenuLateralLayout>
  );
}




// <div className="h-screen  flex flex-col flex-grow  gap-3">
//       {/* HEADER */}
//       <div className="
//         h-12 w-full
//         flex-grow
//         border-dashed border border-zinc-500 rounded-lg"
//       >
//         <p>Header</p>
//       </div>

//       {/* MENU LATERAL  e CONTEÚDO */}
//       <div className="
//         h-full 
//         flex flex-row gap-3"
//       >
//         {/* MENU LATERAL */}
//         <div className="
//           w-72 
//           flex-grow
//           p-2 
//           border-dashed border border-zinc-500 rounded-lg"
//         >
//           <p>Menu Lateral</p>
//           <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Omnis, fugiat ea! Officia autem, unde aut magni, quod vero cum quaerat doloremque aliquam, asperiores laudantium quisquam quae debitis similique. Ut, tempora.</p>
//         </div>


//         {/* CONTEÚDO */}
//         <div className="
//           w-full
//           flex-grow 
//           p-2  
//           border-dashed border border-zinc-500  rounded-lg"
//         >
//           <p>Conteudo</p>
//         </div>
//       </div>


//       {/* FOOTER */}
//       <div className="
//         w-full h-14
//         flex-grow
//         p-2
//         border-dashed border border-zinc-500 
//         rounded-lg">
//         <p>Footer</p>
//       </div>
//     </div>