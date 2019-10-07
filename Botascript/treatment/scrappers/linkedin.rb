require_relative 'network'
# require_relative 'constants' Le fameux number_to_add 80

class Linkedin < NetworkMedia
  # MANDATORY
  # Name should be adapted to the media !
  def connect_linkedin(user, mdp)

    return connect_site do
      access_url("https://www.linkedin.com/login")
      # Add text to a text box
      fill_text_box(:name,"session_key", user)
      fill_text_box(:name,"session_password",mdp)
      click_element(:xpath, "//*[@id='app__container']/main/div/form/div[3]/button")
    end

  end

  def add(args)
    sleep(10)
    p args
    p "L'ordre voudrait que j'add des gens mais pour l'instant je peux pas..."
    @reports["BUG::"]= "We are not yet able to proceed like you asked to."
  end

  def auto_add(username, password)
    number_to_add = 80
    added_guy = 0
    if connect_linkedin(username, password)
      while added_guy < number_to_add

        access_url("https://www.linkedin.com/mynetwork/")

        options = {"html_method": :tag_name,
          "id_string": "button",
          "nb": 3,
          "content": "se connecter"
        }

        guys_to_add = looking_for_list_of_items(options)
        if guys_to_add == false
          @reports["Success:::BUG:::PageLoad"] = "Your program failed after adding #{added_guy} people."
          return @reports
        end
        guys_to_add.reverse.each_with_index do |guy,i|
          if added_guy < number_to_add
            if add_people_from_list(guy)
              added_guy+=1
            else
              if i == 1
                @reports["BUG:::Overload"]= "You were refused to add more people"
                return @reports
              end
            end
          end
        end
      end
    else
      return @reports
    end
    @reports["Success:::"]= "YEAH ! You successfully added #{number_to_add} people."
    return @reports

  end

  def add_people_from_list(guy)
  #==== Ajouter les personnes présents sur la page
    begin
        guy.click
        return true
    rescue
      return false
    end

  end


end
