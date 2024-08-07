/* eslint-disable prettier/prettier */
'user serve'

export async function pedir_material(formulario: any, setGptReposta:any){
    let api_url : string|undefined = process.env.NEXT_PUBLIC_URL_BE;
        
    // URL_BE=be_mpes
    if (api_url != undefined){
        const res = await fetch(api_url, {
            method: 'POST',
            headers: {
                "Access-Control-Allow-Origin" : "*",
                "Content-Type": "application/json",
                "Access-Control-Allow-Methods" : "GET,POST,PUT,DELETE,OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
            },
            body: JSON.stringify(formulario)
        });
    
        if (res.ok) {
            const textoResposta = await res.text();
          // Lógica para quando o envio for bem-sucedido
            console.log('Formulário enviado com sucesso!');
            console.log( textoResposta );
            setGptReposta( textoResposta )
        } else {
          // Lógica para quando houver um erro
            console.error('Erro ao enviar o formulário');
        }
    }
    else{
        console.log("api_url NÃO DEFINIDA");
    }


}