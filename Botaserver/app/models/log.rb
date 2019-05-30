class Log < ApplicationRecord
  belongs_to :order
  validates :order_id, uniqueness: { scope: :exectime}
end
