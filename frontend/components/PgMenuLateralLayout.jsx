/* eslint-disable prettier/prettier */
export default function PgMenuLateralLayout(
    { 
        children = <>Falta o content</>
        , header = <>Falta o header</>
        , menu = <>Falta o menu</>
        , footer = <>Falta o footer</> 
    }
) {
    return (
        <div className="h-screen  flex flex-col flex-grow  gap-2">
            

            {/* HEADER */}
            <div className="
                h-12 w-full
                flex-grow
                p-2
                border-dashed border border-zinc-500 rounded-lg"
            >
                {header}
            </div> {/* HEADER - end*/}
    
            {/* MENU LATERAL  e CONTEÚDO */}
            <div className="
                h-full 
                flex flex-row gap-2"
            >
                {/* MENU LATERAL */}
                <div className="
                    w-72
                    max-w-72 
                    flex-none
                    p-2 
                    border-dashed border border-zinc-500 rounded-lg"
                >
                    {menu}
                </div>
    
    
                {/* CONTEÚDO */}
                <div className="
                    w-full
                    flex-grow 
                    p-2  
                    border-dashed border border-zinc-500  rounded-lg"
                >
                    {children}                
                </div> {/* CONTEÚDO END */}

            </div> {/* MENU LATERAL  e CONTEÚDO END */}
    
    
            {/* FOOTER */}
            <div className="
                w-full h-14
                flex-grow
                p-2
                border-dashed border border-zinc-500 
                rounded-lg"
            >                
                {footer}
            </div> {/* FOOTER END*/}


        </div>  
        
    );
  }
  