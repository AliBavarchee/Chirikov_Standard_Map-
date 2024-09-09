program chirikov_standard_map
  implicit none

  integer, parameter :: dp = selected_real_kind(15, 307)
  integer :: i, n
  real(dp) :: p, x, K
  real(dp), allocatable :: p_array(:), x_array(:)
  
  ! Parameters
  print *, "Enter the number of iterations:"
  read(*,*) n
  print *, "Enter the initial momentum (p):"
  read(*,*) p
  print *, "Enter the initial position (x):"
  read(*,*) x
  print *, "Enter the value of K:"
  read(*,*) K

  ! Allocate arrays for storing the values of p and x
  allocate(p_array(n), x_array(n))

  ! Initialize the initial conditions
  p_array(1) = p
  x_array(1) = x

  ! Iterate the map
  do i = 2, n
     p_array(i) = mod(p_array(i-1) + K * sin(x_array(i-1)), 2.0_dp * 3.14159265358979323846_dp)
     x_array(i) = mod(x_array(i-1) + p_array(i), 2.0_dp * 3.14159265358979323846_dp)
  end do

  ! Output the results
  open(unit=10, file='chirikov_map_data.txt', status='replace')
  do i = 1, n
     write(10,*) p_array(i), x_array(i)
  end do
  close(10)
  print *, "Data has been written to 'chirikov_map_data.txt'."
  
end program chirikov_standard_map
