describe('Login no dashboard', () => {
  it('Coordenador sem permissão não acessa o dashboard', () => {
    cy.visit('https://profzap.jhas.dev/dashboard')
    cy.url().should('include', '/dashboard/login')
    cy.get("input[data-testid='data-testid Username input field']").type('usuariodesconhecido')
    cy.get("input[data-testid='data-testid Password input field']").type('senhainvalida')
    cy.get("button[data-testid='data-testid Login button']").click()
    cy.contains('Invalid username or password').should('be.visible')
  })

  it('Coordenador com credenciais registradas pode acessar o dashboard', () => {
    cy.visit('https://profzap.jhas.dev/dashboard')
    cy.url().should('include', '/dashboard/login')
    cy.get("input[data-testid='data-testid Username input field']").type('admin')
    cy.get("input[data-testid='data-testid Password input field']").type('admintestpass')
    cy.get("button[data-testid='data-testid Login button']").click()
    cy.url().should('include', '/dashboard/d/edxl2fbblo83ke/profzap')
    cy.contains('Pesquisas Por Tema (classificado pelo GPT)').should('be.visible')
  })

})
