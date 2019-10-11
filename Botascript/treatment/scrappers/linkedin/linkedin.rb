require_relative '../network'
require_relative 'relative_namespace'
# require_relative 'constants' Le fameux number_to_add 80

class Linkedin < NetworkMedia
  # MANDATORY
  # Name should be adapted to the media !
  def connect_linkedin(user, mdp)

    return connect_site do
      access_url LINKEDIN_ROUTES_LOGIN
      # Add text to a text box
      fill_text_box(:name, LINKEDIN_SELECTOR_NAMES_USERNAME, user)
      fill_text_box(:name, LINKEDIN_SELECTOR_NAMES_PASSWORD, mdp)
      click_element(:xpath, LINKEDIN_SELECTOR_XPATH_LOGIN_BTN)
    end

  end

  # 0 Combien d'ajout dois-je faire # 1 Se rendre sur la page des adds # 2 LOADING - Faire le scroll down / up jusqua enough profiles # 3 Réunir toutes les cartes à cliquer # 4 Repete 2 et 3 tant que pas assez de profiles to add # 5 Cliquer sur tous les addable_buttons possible dans la limite de nb_add:
  def add(args)
    nb_add = [args["until"], 100 ].min
    access_url LINKEDIN_ROUTES_ADD
    yoyo_scroll nb_of_scroll_needed(nb_add)
    addable_buttons = @browser.find_elements(:css, LINKEDIN_SELECTOR_CSS_ADD_BTN)

    while addable_buttons.size < nb_add
      yoyo_scroll 1
      addable_buttons = @browser.find_elements(:css, LINKEDIN_SELECTOR_CSS_ADD_BTN)
    end

    nb_added_previously = 0
    begin
      addable_buttons.take(nb_add).each_with_index do |btn,i|
        nb_added_previously = i if btn.click
      end
    rescue
      @reports[:WARNING] = "We stopped unconsistently after #{nb_added_previously} adds."
    else
      @reports[:SUCCESS] = "We added #{nb_added_previously} people on #{nb_add}!"
    end
  end






  private # => Until now everything is private !

  def yoyo_scroll(nb=1)
    nb.times do
      scroll_down
      scroll_up(0)
    end
    sleep(3) # Histoire de finir le chargement
  end

  def nb_of_scroll_needed(nb=0)
    # 4 is init number available
    nb -= LINKEDIN_CARDS_INIT_AVAILABLE
    return nb/12 + ( (nb%12 == 0) ? 0 : 1)

  end

end
