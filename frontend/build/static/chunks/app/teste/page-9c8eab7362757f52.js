(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[509],{3594:function(e,t,n){Promise.resolve().then(n.bind(n,910)),Promise.resolve().then(n.bind(n,9352)),Promise.resolve().then(n.bind(n,4867)),Promise.resolve().then(n.bind(n,5714))},910:function(e,t,n){"use strict";n.d(t,{default:function(){return s}});var r=n(7437);function s(){return(0,r.jsx)("div",{children:(0,r.jsx)("h2",{children:"Footer do Sistema"})})}},9352:function(e,t,n){"use strict";n.d(t,{default:function(){return l}});var r=n(7437),s=n(933),a=n(2031),o=n(2265);function l(){let[e,t]=(0,o.useState)({user_id:"",conversar_id:"",pergunta:""}),[n,l]=(0,o.useState)("RESPOSTA INICIAL"),i=async t=>{t.preventDefault();let n=await fetch("http://localhost/api/form_teste",{method:"POST",headers:{"Access-Control-Allow-Origin":"*","Content-Type":"application/json","Access-Control-Allow-Methods":"GET,POST,PUT,DELETE,OPTIONS","Access-Control-Allow-Headers":"Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"},body:JSON.stringify(e)});if(n.ok){let e=await n.text();console.log("Formul\xe1rio enviado com sucesso!"),console.log(e),l(e)}else console.error("Erro ao enviar o formul\xe1rio")};return(0,r.jsxs)("div",{className:" h-screen   flex flex-col  // flex-grow  gap-2 ",children:[(0,r.jsx)("div",{className:"h-[800] min-h-[800] w-[700] overflow-y-scroll border border-gray-300 p-4",children:(0,r.jsx)("div",{className:"h-[800] min-h-[800] w-[700]",dangerouslySetInnerHTML:{__html:n}})}),(0,r.jsxs)("form",{onSubmit:i,className:" container flex flex-col gap-4 justify-end ",children:[(0,r.jsx)(a.Y,{name:"pergunta",type:"text",label:"PERGUNTA",value:e.pergunta,onChange:n=>{let r=n.target.name,s=n.target.value;t({...e,[r]:s}),console.log(e)},className:"w-[700]"}),(0,r.jsx)(s.A,{type:"submit",color:"primary",variant:"solid",className:"w-[300] h-9 mb-28",children:"Submit"})]})]})}},4867:function(e,t,n){"use strict";n.d(t,{default:function(){return s}});var r=n(7437);function s(){return(0,r.jsxs)("div",{className:"flex flex-row gap-4 justify-center",children:[(0,r.jsx)("h2",{className:"font-mono text-lg font-bold",children:"IA Genarativa na Educa\xe7\xe3o"}),(0,r.jsx)("span",{children:"-"}),(0,r.jsx)("h2",{className:"font-mono text-base",children:"Uma ferramenta de suporte a docentes."})]})}},5714:function(e,t,n){"use strict";n.d(t,{default:function(){return u}});var r=n(7437),s=n(933),a=n(5669),o=n(7532),l=n(3061),i=n(7138),c=n(5945),d=n(2857);function u(){return(0,r.jsxs)("div",{children:[(0,r.jsx)(i.default,{href:"/",children:(0,r.jsx)(s.A,{fullWidth:!0,className:"text-base font-bold",color:"primary",css:{paddingLeft:"0px"},variant:"light",children:"Home"})})," ",(0,r.jsx)(c.j,{}),(0,r.jsxs)(o.d,{showDivider:!1,children:[(0,r.jsxs)(l.G,{"aria-label":"Accordion 2",startContent:(0,r.jsx)(d.mLS,{}),title:"Dashboad",children:[(0,r.jsx)(i.default,{href:"/",children:(0,r.jsx)(s.A,{className:"justify-start text-base",color:"primary",startContent:(0,r.jsx)(d.mLS,{}),variant:"light",children:"Painel 01"})}),(0,r.jsx)(i.default,{href:"/",children:(0,r.jsx)(s.A,{fullWidth:!0,className:"justify-start text-base",color:"primary",startContent:(0,r.jsx)(d.mLS,{}),variant:"light",children:"Painel 02"})})]},"2"),(0,r.jsx)(l.G,{"aria-label":"Accordion 3",startContent:(0,r.jsx)(d.qNd,{}),title:"Administra\xe7\xe3o",children:(0,r.jsx)(i.default,{href:"/teste",children:(0,r.jsx)(a.e,{content:"Gerencia Usu\xe1rios [N\xc3O IMPLEMENTADO].",placement:"right-end",children:(0,r.jsx)(s.A,{fullWidth:!0,className:"justify-start text-base",color:"primary",startContent:(0,r.jsx)(d._CL,{}),variant:"light",children:"Gerencia Usu\xe1rios"})})})},"3")]})]})}}},function(e){e.O(0,[680,433,607,79,971,23,744],function(){return e(e.s=3594)}),_N_E=e.O()}]);