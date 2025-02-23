setInterval(() => {
  try {
    // Store element selectors to make them easier to update
    const menuButton = document.querySelector('.edit-account-button.mat-mdc-menu-trigger');
    if (!menuButton) {
      console.log('Menu button not found');
      return;
    }
    menuButton.click();

    // Give the menu time to appear
    setTimeout(() => {
      const menuItems = document.querySelectorAll('.mat-focus-indicator.mat-mdc-menu-item');
      const lastMenuItem = menuItems[menuItems.length - 1];
      if (!lastMenuItem) {
        console.log('Menu item not found');
        return;
      }
      lastMenuItem.click();

      // Give time for confirmation dialog
      setTimeout(() => {
        const confirmButton = document.querySelector('.confirm-button.mat-mdc-raised-button');
        if (!confirmButton) {
          console.log('Confirm button not found');
          return;
        }
        confirmButton.click();
      }, 200);
    }, 200);

  } catch (error) {
    console.error('Error:', error);
  }
}, 1000);
