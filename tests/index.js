describe('Google Search Bar Test', () => {
  it('should check if the search bar is present on Google', () => {
    // Visit Google
    cy.visit('https://www.google.com');

    // Check if the search bar is present
    cy.get('input[name="q"]').should('be.visible');
  });
});
